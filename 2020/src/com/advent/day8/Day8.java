package com.advent.day8;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Day8 {

    public static void main(String[] args) throws FileNotFoundException {
        partOne();
        partTwo();
    }

    public static void partOne() throws FileNotFoundException {
        List<String> instructionStrings = getInstructions();
        List<Instruction> instructions = instructionStrings.stream()
                .map(Instruction::new).collect(Collectors.toList());

        Computer computer = new Computer();
        computer.runProgramOnce(instructions);

        System.out.println("Answer to Day 8 Part 1 = " + computer.getAcc());
    }

    public static void partTwo() throws FileNotFoundException {
        List<String> instructionStrings = getInstructions();
        List<Instruction> instructions = instructionStrings.stream()
                .map(Instruction::new).collect(Collectors.toList());

        Computer computer = new Computer();
        computer.runProgramToTermination(instructions);

        System.out.println("Answer to Day 8 Part 2 = " + computer.getAcc());
    }

    private static List<String> getInstructions() throws FileNotFoundException {
        List<String> result = new ArrayList<>();
        Scanner scanner =
                new Scanner(
                        new File("/Users/zackgrim/Documents/adventofcode/2020/src/com/advent/data/day8.input")
                );

        scanner.useDelimiter("\\n");

        while (scanner.hasNext()) {
            result.add(scanner.next());
        }

        return result;
    }
}
