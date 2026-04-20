package untitled.src;
import org.json.JSONArray;

import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {

        System.out.println("Please enter the github user you want to check up on : ");
        Scanner scan = new Scanner(System.in);
        String input = scan.nextLine();
        String[] command =input.split(" ");
        ArgsParser.isValid(command);
        System.out.println("Entry is valid. Fetching data...");
        String storedData = GitFetcher.fetch("https://api.github.com/users/" +command[0] + "/events");
//          String storedData = GitFetcher.fetch("https://api.github.com/users/matata808/events");
        JSONArray json = new JSONArray(storedData);
        JSONDisplayer.translateUserActivity(json);
    }
}