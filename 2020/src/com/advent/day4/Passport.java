package com.advent.day4;


import lombok.Builder;
import lombok.NonNull;
import lombok.RequiredArgsConstructor;
import lombok.Value;

@Value
@RequiredArgsConstructor
@Builder
public class Passport {
    @NonNull
    String birthYear;

    @NonNull
    String issueYear;

    @NonNull
    String expirationYear;

    @NonNull
    String height;

    @NonNull
    String hairColor;

    @NonNull
    String eyeColor;

    @NonNull
    String passportId;

    String countryId;

    public boolean validatePassport() {
        return (birthYear != null && issueYear != null && expirationYear != null && height != null && hairColor != null
            && eyeColor != null && passportId != null);
    }
}
