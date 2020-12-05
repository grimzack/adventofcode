package com.advent.day4;

import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class PassportValidator {

    private static final Set<String> validEyeColors =
            Stream.of("amb", "blu", "brn", "gry", "grn", "hzl", "oth").collect(Collectors.toSet());

    public static boolean validate(Passport passport) {
        return (validateBirthYear(passport.getBirthYear())
                && validateIssueYear(passport.getIssueYear())
                && validateExpYear(passport.getExpirationYear())
                && validateHeight(passport.getHeight())
                && validateHairColor(passport.getHairColor())
                && validateEyeColor(passport.getEyeColor())
                && validatePassportId(passport.getPassportId()));
    }

    private static Matcher getYearMatcher(String value) {
        Pattern pattern = Pattern.compile("^[0-9]{4}");
        return pattern.matcher(value);
    }

    public static boolean validateBirthYear(String value) {
        Matcher matcher = getYearMatcher(value);

        if (matcher.matches()) {
            int year = Integer.parseInt(matcher.group(0));
            return (year >= 1920 && year <= 2002);
        }

        return false;
    }

    public static boolean validateIssueYear(String value) {
        Matcher matcher = getYearMatcher(value);

        if (matcher.matches()) {
            int year = Integer.parseInt(matcher.group(0));
            return (year >= 2010 && year <= 2020);
        }

        return false;
    }

    public static boolean validateExpYear(String value) {
        Matcher matcher = getYearMatcher(value);

        if (matcher.matches()) {
            int year = Integer.parseInt(matcher.group(0));
            return (year >= 2020 && year <= 2030);
        }

        return false;
    }

    public static boolean validateHeight(String value) {
        Pattern pattern = Pattern.compile("^([0-9]{2,3})([a-z]{2})");
        Matcher matcher = pattern.matcher(value);

        if (matcher.matches()) {
            int height = Integer.parseInt(matcher.group(1));
            String unit = matcher.group(2);

            if (unit.equals("cm")) {
                return (height >= 150 && height <= 193);
            } else if (unit.equals("in")) {
                return (height >= 59 && height <= 76);
            }
        }

        return false;
    }

    public static boolean validateHairColor(String value) {
        Pattern pattern = Pattern.compile("^#([abcdef0-9]{6})");
        Matcher matcher = pattern.matcher(value);

        return matcher.matches();
    }

    public static boolean validateEyeColor(String value) {
        return (validEyeColors.contains(value));
    }

    public static boolean validatePassportId(String value) {
        Pattern pattern = Pattern.compile("^[0-9]{9}");
        Matcher matcher = pattern.matcher(value);

        return matcher.matches();
    }
}
