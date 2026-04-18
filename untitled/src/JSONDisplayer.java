import org.json.JSONArray;
import org.json.JSONObject;
public class JSONDisplayer {
    String response;

    JSONObject json = new JSONObject(response);
    public JSONDisplayer(String response) {
        this.response = response;
    }

}
