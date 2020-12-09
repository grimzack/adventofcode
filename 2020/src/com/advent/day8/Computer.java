package com.advent.day8;

import lombok.Getter;
import lombok.Setter;

import java.util.List;
import java.util.Stack;

@Getter
@Setter
public class Computer {
    int ptr;
    int acc;

    public Computer() {
        ptr = 0;
        acc = 0;
    }

    public void runProgramOnce(List<Instruction> instructionList) {
        Instruction curInstr;
        while (ptr < instructionList.size()) {
            curInstr = instructionList.get(ptr);
            if (curInstr.getTimesExecuted() > 0) break;

            executeInstruction(curInstr);
        }
    }

    public void runProgramToTermination(List<Instruction> instructionList) {
        Instruction curInstr;
        Stack<Instruction> instrPath = new Stack<>();
        Stack<Integer> accStack = new Stack<>();
        Stack<Integer> ptrStack = new Stack<>();
        accStack.push(acc);
        ptrStack.push(ptr);
        while (ptr < instructionList.size()) {
            curInstr = instructionList.get(ptr);
            if (curInstr.getTimesExecuted() > 0) {
                acc = accStack.pop();
                ptr = ptrStack.pop();
                Instruction newInstr = instrPath.pop();
                newInstr.setTimesExecuted(0);

                while (!newInstr.getInstruction().equals("jmp") && !newInstr.getInstruction().equals("nop")) {
                    newInstr = instrPath.pop();
                    newInstr.setTimesExecuted(0);
                    acc = accStack.pop();
                    ptr = ptrStack.pop();

                    if (newInstr.isWasChanged()) {
                        if (newInstr.getInstruction().equals("jmp")) {
                            newInstr.setInstruction("nop");
                        } else {
                            newInstr.setInstruction("jmp");
                        }

                        newInstr = instrPath.pop();
                        newInstr.setTimesExecuted(0);
                        acc = accStack.pop();
                        ptr = ptrStack.pop();
                    }
                }

                if (newInstr.getInstruction().equals("jmp")) {
                    newInstr.setInstruction("nop");
                } else {
                    newInstr.setInstruction("jmp");
                }

                newInstr.setWasChanged(true);
            } else {
                executeInstruction(curInstr);
                instrPath.push(curInstr);
                accStack.push(acc);
                ptrStack.push(ptr);
            }

        }
    }

    private void executeInstruction(Instruction instruction) {
        switch (instruction.getInstruction()) {
            case "nop":
                instruction.setTimesExecuted(instruction.getTimesExecuted() + 1);
                ptr++;
                break;
            case "acc":
                acc += instruction.getValue();
                instruction.setTimesExecuted(instruction.getTimesExecuted() + 1);
                ptr++;
                break;
            case "jmp":
                ptr += instruction.getValue();
                instruction.setTimesExecuted(instruction.getTimesExecuted() + 1);
                break;
            default:
                break;
        }
    }
}
