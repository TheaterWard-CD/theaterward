package com.abcd.theaterward.domain;

import jakarta.persistence.*;

@Entity
@Table(name = "ssr")
public class Ssr {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "reviews_no")
    private int reviewNo;

    @Column(name = "theater_no")
    private int theaterNo;

    @Column(name = "seat_no")
    private int seatNo;

    @Column(name = "shows_name")
    private String showName;

    @Column(name = "shows_year")
    private int showYear;

    @ManyToOne
    @JoinColumn(name = "reviews_no", insertable = false, updatable = false)
    private Reviews reviews;

    public int getReviewNo() {
        return reviewNo;
    }

    public void setReviewNo(int reviewNo) {
        this.reviewNo = reviewNo;
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
}
