package com.abcd.theaterward.domain;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "seat_shows")
public class SeatShows {

    @Id
    @Column(name = "shows_name")
    private String showName;

    @Id
    @Column(name = "shows_year")
    private int showYear;

    @Id
    @Column(name = "theater_no")
    private int theaterNo;

    @Id
    @Column(name = "seat_no")
    private int seatNo;

    @Column(name = "seat_shows_grade")
    private String grade;

    @Column(name = "seats_shows_price")
    private int price;

    public String getShowName() {
        return showName;
    }

    public void setShowName(String showName) {
        this.showName = showName;
    }

    public int getShowYear() {
        return showYear;
    }

    public void setShowYear(int showYear) {
        this.showYear = showYear;
    }

    public int getTheaterNo() {
        return theaterNo;
    }

    public void setTheaterNo(int theaterNo) {
        this.theaterNo = theaterNo;
    }

    public int getSeatNo() {
        return seatNo;
    }

    public void setSeatNo(int seatNo) {
        this.seatNo = seatNo;
    }

    public String getGrade() {
        return grade;
    }

    public void setGrade(String grade) {
        this.grade = grade;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
}
