package com.advent;

import com.advent.day1.Day1;
import com.advent.day2.Day2;

import java.io.IOException;

public class Main {

    public static void main(String[] args) throws IOException {
//        int answer1 = Day1.partOne();
//        int answer2 = Day1.partTwo();
        int answer1 = Day2.partOne();
        int answer2 = Day2.partTwo();

        System.out.println("Answer 1 = " + answer1);
        System.out.println("Answer 2 = " + answer2);
    }
}
