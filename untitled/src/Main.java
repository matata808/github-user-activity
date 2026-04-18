import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner scan = new Scanner(System.in);
        String input = scan.nextLine();
        String[] command =input.split(" ");
        ArgsParser.isValid(command);
        System.out.println("Entry is valid. Fetching data...");
        String storedData = GitFetcher.fetch("https://api.github.com/users/" +command[0] + "/events");
        System.out.println(storedData);
        JSONDisplayer displayer = new JSONDisplayer(storedData);

    }
}