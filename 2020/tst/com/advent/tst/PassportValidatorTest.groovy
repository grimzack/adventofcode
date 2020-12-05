package com.advent.tst

import com.advent.day4.PassportValidator
import spock.lang.Specification

class PassportValidatorTest extends Specification {

    def "valid birth year returns true"() {
        given:
        String field = "1990"

        when:
        boolean isValid = PassportValidator.validateBirthYear(field)

        then:
        isValid
    }

    def "invalid birth years return false"() {
        given:
        String field1 = "abcd"
        String field2 = ""
        String field3 = "1234"

        when:
        boolean isValid1 = PassportValidator.validateBirthYear(field1)
        boolean isValid2 = PassportValidator.validateBirthYear(field2)
        boolean isValid3 = PassportValidator.validateBirthYear(field3)

        then:
        !isValid1
        !isValid2
        !isValid3
    }

    def "valid hair color returns true"() {
        given:
        String field1 = "#aaaaaa"
        String field2 = "#000000"

        when:
        boolean isValid1 = PassportValidator.validateHairColor(field1)
        boolean isValid2 = PassportValidator.validateHairColor(field2)

        then:
        isValid1
        isValid2
    }

    def "invalid hair color return false"() {
        given:
        String field1 = "abcd"
        String field2 = ""
        String field3 = "1234"

        when:
        boolean isValid1 = PassportValidator.validateBirthYear(field1)
        boolean isValid2 = PassportValidator.validateBirthYear(field2)
        boolean isValid3 = PassportValidator.validateBirthYear(field3)

        then:
        !isValid1
        !isValid2
        !isValid3
    }

    def "test byrs"() {
        given:
        String val1 = "2002"
        String val2 = "2003"

        when:
        boolean valid1 = PassportValidator.validateBirthYear(val1)
        boolean valid2 = PassportValidator.validateBirthYear(val2)

        then:
        valid1
        !valid2
    }

    def "test hgts"() {
        given:
        String val1 = "60in"
        String val2 = "190cm"
        String val3 = "190in"
        String val4 = "190"

        when:
        boolean valid1 = PassportValidator.validateHeight(val1)
        boolean valid2 = PassportValidator.validateHeight(val2)
        boolean valid3 = PassportValidator.validateHeight(val3)
        boolean valid4 = PassportValidator.validateHeight(val4)

        then:
        valid1
        valid2
        !valid3
        !valid4
    }

    def "test pids"() {
        given:
        String val1 = "000000001"
        String val2 = "0123456789"

        when:
        boolean valid1 = PassportValidator.validatePassportId(val1)
        boolean valid2 = PassportValidator.validatePassportId(val2)

        then:
        valid1
        !valid2
    }
}
