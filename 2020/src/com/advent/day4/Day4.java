package com.advent.day4;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Day4 {
    public static void partOne() throws FileNotFoundException {
        List<Passport> passports = parseInput();
        int validPassports = 0;

        for (Passport pass : passports) {
            if (pass != null) validPassports++;
        }

        System.out.println("Answer to Day 4 Part 1 = " + validPassports);
    }

    public static void partTwo() throws FileNotFoundException {
        List<Passport> passports = parseInput();
        int validPassports = 0;

        for (Passport passport : passports) {
            if (passport != null && PassportValidator.validate(passport)) validPassports++;
        }

        System.out.println("Answer to Day 4 Part 2 = " + validPassports);
    }

    private static List<Passport> parseInput() throws FileNotFoundException {
        List<String> result = new ArrayList<>();
        Scanner scanner =
                new Scanner(
                    new File("/Users/zackgrim/Documents/adventofcode/2020/src/com/advent/data/day4.input")
                );

        scanner.useDelimiter("\\n\\n");

        while (scanner.hasNext()) {
            result.add(scanner.next());
        }

        List<String> passportStrings = result.stream().map(str -> str.replace('\n', ' '))
                .collect(Collectors.toList());

        List<Passport> passports = new ArrayList<>();
        for (String pass : passportStrings) {
            passports.add(convertStringToPassport(pass));
        }

        return passports;
    }

    private static Passport convertStringToPassport(String passString) {
        List<String> fields = Arrays.asList(passString.split(" "));

        Map<String, String> fieldMap = fields.stream()
                .map(str -> str.split(":"))
                .collect(Collectors.toMap(str -> str[0], str -> str[1]));

        try {
            return Passport.builder()
                    .birthYear(fieldMap.get("byr"))
                    .expirationYear(fieldMap.get("eyr"))
                    .issueYear(fieldMap.get("iyr"))
                    .height(fieldMap.get("hgt"))
                    .hairColor(fieldMap.get("hcl"))
                    .eyeColor(fieldMap.get("ecl"))
                    .passportId(fieldMap.get("pid"))
                    .countryId(fieldMap.get("cid"))
                    .build();
        } catch (Exception e) {
            return null;
        }
    }
}
