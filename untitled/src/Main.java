import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        String input = scan.nextLine();
        String[] command =input.split(" ");
        ArgsParser.isValid(command);
        System.out.println(command[0]);

    }
}