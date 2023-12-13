package com.abcd.theaterward.domain;

public class ReviewInfo {

    private String userId;

    private int reviewScore;

    private String reviewContent;

    private int theaterNo;

    private int seatNo;

    private String showName;

    private int showYear;

    public String getUserId() {
        return userId;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }

    public int getReviewScore() {
        return reviewScore;
    }

    public void setReviewScore(int reviewScore) {
        this.reviewScore = reviewScore;
    }

    public String getReviewContent() {
        return reviewContent;
    }

    public void setReviewContent(String reviewContent) {
        this.reviewContent = reviewContent;
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
