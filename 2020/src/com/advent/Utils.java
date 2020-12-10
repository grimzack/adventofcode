package com.advent;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

public class Utils {

    public static List<String> getInputAsStrings(String day) throws IOException {
        String PATH_TO_INPUT = "/Users/zackgrim/Documents/adventofcode/2020/src/com/advent/data/" + day + ".input";
        Path inputPath = Paths.get(PATH_TO_INPUT);
        return Files.readAllLines(inputPath, StandardCharsets.UTF_8);
    }

    public static List<Integer> getInputAsInts(String day) throws IOException {
        return getInputAsStrings(day).stream().map(Integer::parseInt).collect(Collectors.toList());
    }

    public static List<Long> getInputAsLongs(String day) throws IOException {
        return getInputAsStrings(day).stream().map(Long::parseLong).collect(Collectors.toList());
    }

    public static int countCharsInString(String inStr, char targetChar) {
        int count = 0;

        for (int i = 0; i < inStr.length(); i++) {
            if (inStr.charAt(i) == targetChar) count++;
        }

        return count;
    }
}
