package com.advent;

import com.advent.day3.Day3;
import com.advent.day4.Day4;

import java.io.IOException;

public class Main {

    public static void main(String[] args) throws IOException {
        int answer1 = Day4.partOne();
        long answer2 = Day4.partTwo();

        System.out.println("Answer 1 = " + answer1);
        System.out.println("Answer 2 = " + answer2);
    }
}
