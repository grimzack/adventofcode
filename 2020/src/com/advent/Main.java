package com.advent;

import com.advent.day1.Day1Part1;
import com.advent.day1.Day1Part2;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) throws IOException {
        Path inputPath =
                Paths.get("/Users/zackgrim/Documents/adventofcode/2020/src/com/company/data/day1_1.input");
        List<String> inputAsString = Files.readAllLines(inputPath, StandardCharsets.UTF_8);
        List<Integer> inputAsInts = inputAsString.stream().map(Integer::parseInt).collect(Collectors.toList());

        int answer1 = Day1Part1.findProduct(inputAsInts);
        int answer2 = Day1Part2.findProduct(inputAsInts);

        System.out.println("Answer 1 = " + answer1);
        System.out.println("Answer 2 = " + answer2);
    }
}
