package untitled.src;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class JSONDisplayer {

    public static void translateUserActivity(JSONArray jsonArray) {
        HashMap<String, Integer> pushCount = new HashMap<>();
        List<String> otherEvents = new ArrayList<>();

        for (int i = 0; i < jsonArray.length(); i++) {
            JSONObject event = jsonArray.getJSONObject(i);

            String type = event.getString("type");
            String repoName = event.getJSONObject("repo").getString("name");

            switch (type) {
                case "PushEvent":
                    pushCount.merge(repoName, 1, Integer::sum);
                    break;
                case "PullRequestEvent":
                    String action = event.getJSONObject("payload").getString("action");
                    otherEvents.add("Pull Request " + action + " in " + repoName);
                    break;
                case "CreateEvent":
                    String refType = event.getJSONObject("payload").getString("ref_type");
                    otherEvents.add("Created a new " + refType + " in " + repoName);
                    break;
                case "DeleteEvent":
                    String ref = event.getJSONObject("payload").getString("ref");
                    otherEvents.add("Deleted branch '" + ref + "' in " + repoName);
                    break;
                case "WatchEvent":
                    otherEvents.add("Starred " + repoName);
                    break;
                case "IssuesEvent":
                    String issueAction = event.getJSONObject("payload").getString("action");
                    otherEvents.add("Opened a new issue in " + repoName);
                    break;
                default:
                    otherEvents.add("Unknown event: " + type + " in " + repoName);
            }
        }

        // Print push summaries first
        for (Map.Entry<String, Integer> entry : pushCount.entrySet()) {
            System.out.println("- Pushed " + entry.getValue() + " commits to " + entry.getKey());
        }

        // Then print everything else
        for (String line : otherEvents) {
            System.out.println("- " + line);
        }
    }


}
