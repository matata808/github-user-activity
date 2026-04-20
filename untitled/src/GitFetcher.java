package untitled.src;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.URL;

public class GitFetcher {
    
    public static String fetch(String url) throws IOException {
        URL url1 = new URL(url);
        InputStream inputStream = url1.openConnection().getInputStream();
        BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));
        String line;
        StringBuilder builder = new StringBuilder();
        while ((line = reader.readLine() ) != null){
            builder.append(line);
        }
        reader.close();
        return builder.toString();
    }
    
    
    
    
}
