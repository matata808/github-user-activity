package untitled.src;

public class ArgsParser {

    public static String isValid(String[] command) {
        if (command.length == 0){
            throw new IllegalArgumentException("Invalid entry. Please Try again");
        }

        if (command[0].isEmpty() ||command[0].isBlank()){throw new IllegalArgumentException("Invalid entry. Please Try again");}

        try {
            Integer.parseInt(command[0]);
            throw new IllegalArgumentException("entry is not valid. Try again.");
        } catch (NumberFormatException ignored) {
        }

        return command[0];

    }


}
