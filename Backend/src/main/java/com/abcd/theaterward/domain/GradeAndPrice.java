package com.abcd.theaterward.domain;

public class GradeAndPrice {
    private String seatShowsGrade;

    private int seatShowsPrice;

    public String getSeatShowsGrade() {
        return seatShowsGrade;
    }

    public void setSeatShowsGrade(String seatShowsGrade) {
        this.seatShowsGrade = seatShowsGrade;
    }

    public int getSeatShowsPrice() {
        return seatShowsPrice;
    }

    public void setSeatShowsPrice(int seatShowsPrice) {
        this.seatShowsPrice = seatShowsPrice;
    }

    public GradeAndPrice(SeatShows ss) {
        this.seatShowsGrade = ss.getGrade();
        this.seatShowsPrice = ss.getPrice();
    }
}
