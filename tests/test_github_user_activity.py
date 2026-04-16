import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

import github_user_activity


class GithubUserActivityTests(unittest.TestCase):
    @patch("github_user_activity.urllib.request.urlopen")
    def test_fetch_user_activity_returns_decoded_json(self, mock_urlopen):
        response = MagicMock()
        response.read.return_value = b'[{"type":"PushEvent"}]'
        response.__enter__.return_value = response
        mock_urlopen.return_value = response

        result = github_user_activity.fetch_user_activity("octocat")

        self.assertEqual(result, [{"type": "PushEvent"}])


    @patch("github_user_activity.urllib.request.urlopen")
    @patch.dict("os.environ", {"GITHUB_TOKEN": "secret-token"}, clear=False)
    def test_fetch_user_activity_uses_token_header_when_available(self, mock_urlopen):
        response = MagicMock()
        response.read.return_value = b'[]'
        response.__enter__.return_value = response
        mock_urlopen.return_value = response

        github_user_activity.fetch_user_activity("octocat")

        request = mock_urlopen.call_args.args[0]
        self.assertEqual(request.get_header("Authorization"), "Bearer secret-token")

    def test_fetch_command_saves_json_file(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            output_file = Path(tmp_dir) / "activity.json"
            with patch("github_user_activity.fetch_user_activity", return_value=[{"id": "1"}]):
                exit_code = github_user_activity.main(["fetch", "octocat", "--output", str(output_file)])

            self.assertEqual(exit_code, 0)
            self.assertTrue(output_file.exists())
            self.assertEqual(json.loads(output_file.read_text(encoding="utf-8")), [{"id": "1"}])

    def test_show_command_prints_json(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            input_file = Path(tmp_dir) / "activity.json"
            input_file.write_text('[{"id":"1"}]', encoding="utf-8")

            with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
                exit_code = github_user_activity.main(["show", "--input", str(input_file)])

            self.assertEqual(exit_code, 0)
            self.assertIn('"id": "1"', mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
