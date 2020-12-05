package com.advent.day2;

import com.advent.Utils;

import java.io.IOException;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day2 {
    private static final String DAY = "day2";

    public static void partOne() throws IOException {
        List<String> input = Utils.getInputAsStrings(DAY);

        System.out.println("Answer to Day 2 Part 1 = " + input.stream().filter(Day2::matchesPolicy).count());
    }

    public static void partTwo() throws IOException {
        List<String> input = Utils.getInputAsStrings(DAY);

        System.out.println("Answer to Day 2 Part 2 = " +
                input.stream().filter(Day2::matchesOfficialTobogganCorporatePolicy).count());
    }

    private static boolean matchesPolicy(String input) {
        PasswordPolicy policy = PasswordPolicy.newPolicy(input);

        int count = Utils.countCharsInString(policy.password, policy.character);

        return ((count >= policy.firstBound) && (count <= policy.lastBound));
    }

    private static boolean matchesOfficialTobogganCorporatePolicy(String input) {
        PasswordPolicy policy = PasswordPolicy.newPolicy(input);

        return ((policy.password.charAt(policy.firstBound - 1) == policy.character) ^
                    (policy.password.charAt(policy.lastBound - 1) == policy.character));
    }

    static class PasswordPolicy {
        int firstBound;
        int lastBound;
        char character;
        String password;

        public PasswordPolicy(int firstBound, int lastBound, char character, String password) {
            this.firstBound = firstBound;
            this.lastBound = lastBound;
            this.character = character;
            this.password = password;
        }

        private static PasswordPolicy newPolicy(String policyPassword) {
            Pattern pattern = Pattern.compile("^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)$");
            Matcher matcher = pattern.matcher(policyPassword);
            matcher.matches();

            int minimum = Integer.parseInt(matcher.group(1));
            int maximum = Integer.parseInt(matcher.group(2));

            return new PasswordPolicy(minimum, maximum, matcher.group(3).charAt(0), matcher.group(4));
        }
    }


}
