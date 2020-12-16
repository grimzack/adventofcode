package com.advent.day11;

import com.advent.Utils;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Day11 {
    private static final String DAY = "day11";
    private static final String SAMPLE = "sample";

    private static final char EMPTY_SEAT = 'L';
    private static final char OCCUPIED_SEAT = '#';
    private static final char FLOOR = '.';

    enum DIRECTION {
        N,
        NE,
        E,
        SE,
        S,
        SW,
        W,
        NW
    }

    public static void main(String[] args) throws IOException {
        partOne();
        partTwo();
    }

    public static void partOne() throws IOException {
        List<List<Character>> inputAsChars = performSetup();

        calculateSeating(inputAsChars);
        int answer = countOccupiedSeats(inputAsChars);

        System.out.println("Answer to Day 11 Part 1 = " + answer);
    }

    public static void partTwo() throws IOException {
        List<List<Character>> inputAsChars = performSetup();

        calculateVisibleSeating(inputAsChars);
        int answer = countOccupiedSeats(inputAsChars);

        System.out.println("Answer to Day 11 Part 2 = " + answer);
    }

    private static List<List<Character>> performSetup() throws IOException {
        List<String> input = Utils.getInputAsStrings(DAY);
        List<List<Character>> inputAsChars = new ArrayList<>();

        for (String str : input) {
            List<Character> charList = str.chars().mapToObj(c -> (char) c).collect(Collectors.toList());
            inputAsChars.add(charList);
        }

        return inputAsChars;
    }

    private static int countOccupiedSeats(List<List<Character>> inputAsChars) {
        int numOccupied = 0;
        for (List<Character> chars : inputAsChars) {
            for (char c : chars) {
                if (isOccupiedSeat(c)) numOccupied++;
            }
        }

        return numOccupied;
    }

    private static void calculateSeating(List<List<Character>> inputAsChars) {
        List<List<Character>> inputClone = inputAsChars.stream().map(ArrayList::new).collect(Collectors.toList());

        while (true) {
            processSeatingRotation(inputAsChars);

            if (inputAsChars.equals(inputClone)) break;

            inputClone = inputAsChars.stream().map(ArrayList::new).collect(Collectors.toList());
        }
    }

    private static void processSeatingRotation(List<List<Character>> inputAsChars) {
        List<List<Character>> inputCopy = inputAsChars.stream().map(ArrayList::new).collect(Collectors.toList());
        for (int row = 0; row < inputAsChars.size(); row++) {
            for (int column = 0; column < inputAsChars.get(0).size(); column++) {
                char seat = inputAsChars.get(row).get(column);

                if (isSeat(seat)) {
                    int numAdjacentOccupied = countAdjacentOccupied(row, column, inputCopy);
                    if (isOccupiedSeat(seat) && numAdjacentOccupied >= 4) {
                        inputAsChars.get(row).set(column, EMPTY_SEAT);
                    } else if (isEmptySeat(seat) && numAdjacentOccupied == 0) {
                        inputAsChars.get(row).set(column, OCCUPIED_SEAT);
                    }
                }
            }
        }
    }

    private static int countAdjacentOccupied(int row, int column, List<List<Character>> inputAsChars) {
        int numOccupied = 0;
        for (int r = (row - 1); r <= (row + 1); r++) {
            for (int c = (column - 1); c <= (column + 1); c++) {
                if (outOfBounds(r, c, inputAsChars.size(), inputAsChars.get(0).size(), row, column)) continue;
                if (isOccupiedSeat(inputAsChars.get(r).get(c))) numOccupied++;
            }
        }

        return numOccupied;
    }

    private static void calculateVisibleSeating(List<List<Character>> inputAsChars) {
        List<List<Character>> inputClone = inputAsChars.stream().map(ArrayList::new).collect(Collectors.toList());

        while (true) {
            processVisibleSeatingRotation(inputAsChars);

            if (inputAsChars.equals(inputClone)) break;

            inputClone = inputAsChars.stream().map(ArrayList::new).collect(Collectors.toList());
        }
    }

    private static void processVisibleSeatingRotation(List<List<Character>> inputAsChars) {
        List<List<Character>> inputCopy = inputAsChars.stream().map(ArrayList::new).collect(Collectors.toList());
        for (int row = 0; row < inputAsChars.size(); row++) {
            for (int column = 0; column < inputAsChars.get(0).size(); column++) {
                char seat = inputAsChars.get(row).get(column);

                if (isSeat(seat)) {
                    int numAdjacentOccupied = countVisibleOccupied(row, column, inputCopy);
                    if (isOccupiedSeat(seat) && numAdjacentOccupied >= 5) {
                        inputAsChars.get(row).set(column, EMPTY_SEAT);
                    } else if (isEmptySeat(seat) && numAdjacentOccupied == 0) {
                        inputAsChars.get(row).set(column, OCCUPIED_SEAT);
                    }
                }
            }
        }
    }

    private static int countVisibleOccupied(int row, int col, List<List<Character>> inputAsChars) {
        int numOccupied = 0;

        // Count cardinals
        numOccupied += lookForSeat(row, col, inputAsChars, DIRECTION.NW);
        numOccupied += lookForSeat(row, col, inputAsChars, DIRECTION.N);
        numOccupied += lookForSeat(row, col, inputAsChars, DIRECTION.NE);
        numOccupied += lookForSeat(row, col, inputAsChars, DIRECTION.E);
        numOccupied += lookForSeat(row, col, inputAsChars, DIRECTION.SE);
        numOccupied += lookForSeat(row, col, inputAsChars, DIRECTION.S);
        numOccupied += lookForSeat(row, col, inputAsChars, DIRECTION.SW);
        numOccupied += lookForSeat(row, col, inputAsChars, DIRECTION.W);

        return numOccupied;
    }

    private static int lookForSeat(int row, int col, List<List<Character>> input, DIRECTION dir) {
        int beginningRow = row;
        int beginningCol = col;
        char curSeat;
        switch(dir) {
            case NW:
                while (true) {
                    row--;
                    col--;
                    if (outOfBounds(row, col, input.size(), input.get(0).size(), beginningRow, beginningCol))
                        break;
                    curSeat = input.get(row).get(col);
                    if (isSeat(curSeat)) {
                        if (isOccupiedSeat(curSeat)) return 1;
                        break;
                    }
                }
                break;
            case N:
                while (true) {
                    row--;
                    if (outOfBounds(row, col, input.size(), input.get(0).size(), beginningRow, beginningCol))
                        break;
                    curSeat = input.get(row).get(col);
                    if (isSeat(curSeat)) {
                        if (isOccupiedSeat(curSeat)) return 1;
                        break;
                    }
                }
                break;
            case NE:
                while (true) {
                    row--;
                    col++;
                    if (outOfBounds(row, col, input.size(), input.get(0).size(), beginningRow, beginningCol))
                        break;
                    curSeat = input.get(row).get(col);
                    if (isSeat(curSeat)) {
                        if (isOccupiedSeat(curSeat)) return 1;
                        break;
                    }
                }
                break;
            case E:
                while (true) {
                    col++;
                    if (outOfBounds(row, col, input.size(), input.get(0).size(), beginningRow, beginningCol))
                        break;
                    curSeat = input.get(row).get(col);
                    if (isSeat(curSeat)) {
                        if (isOccupiedSeat(curSeat)) return 1;
                        break;
                    }
                }
                break;
            case SE:
                while (true) {
                    row++;
                    col++;
                    if (outOfBounds(row, col, input.size(), input.get(0).size(), beginningRow, beginningCol))
                        break;
                    curSeat = input.get(row).get(col);
                    if (isSeat(curSeat)) {
                        if (isOccupiedSeat(curSeat)) return 1;
                        break;
                    }
                }
                break;
            case S:
                while (true) {
                    row++;
                    if (outOfBounds(row, col, input.size(), input.get(0).size(), beginningRow, beginningCol))
                        break;
                    curSeat = input.get(row).get(col);
                    if (isSeat(curSeat)) {
                        if (isOccupiedSeat(curSeat)) return 1;
                        break;
                    }
                }
                break;
            case SW:
                while (true) {
                    row++;
                    col--;
                    if (outOfBounds(row, col, input.size(), input.get(0).size(), beginningRow, beginningCol))
                        break;
                    curSeat = input.get(row).get(col);
                    if (isSeat(curSeat)) {
                        if (isOccupiedSeat(curSeat)) return 1;
                        break;
                    }
                }
                break;
            case W:
                while (true) {
                    col--;
                    if (outOfBounds(row, col, input.size(), input.get(0).size(), beginningRow, beginningCol))
                        break;
                    curSeat = input.get(row).get(col);
                    if (isSeat(curSeat)) {
                        if (isOccupiedSeat(curSeat)) return 1;
                        break;
                    }
                }
                break;
            default:
                return 0;
        }

        return 0;
    }

    private static boolean outOfBounds(int row, int column, int rows, int columns, int targetRow, int targetCol) {
        return (row < 0 || column < 0 || row >= rows || column >= columns || (row == targetRow && column == targetCol));
    }

    private static boolean isSeat(char seat) {
        return (isEmptySeat(seat) || isOccupiedSeat(seat));
    }

    private static boolean isEmptySeat(char seat) {
        return (seat == EMPTY_SEAT);
    }

    private static boolean isOccupiedSeat(char seat) {
        return (seat == OCCUPIED_SEAT);
    }

    private static int calculateEmptySeats(List<List<Character>> inputAsChars) {
        return 0;
    }
}
