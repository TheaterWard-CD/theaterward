package com.abcd.theaterward.domain;

public class ReviewResponseByTheater {
    private int reviewNo;

    private int reviewScore;

    private String userId;

    private String reviewContent;

    private String showName;

    private int showYear;

    public ReviewResponseByTheater(int reviewNo, int reviewScore, String userId, String reviewContent, String showName, int showYear) {
        this.reviewNo = reviewNo;
        this.reviewScore = reviewScore;
        this.userId = userId;
        this.reviewContent = reviewContent;
        this.showName = showName;
        this.showYear = showYear;
    }

    public int getReviewNo() {
        return reviewNo;
    }

    public void setReviewNo(int reviewNo) {
        this.reviewNo = reviewNo;
    }

    public int getReviewScore() {
        return reviewScore;
    }

    public void setReviewScore(int reviewScore) {
        this.reviewScore = reviewScore;
    }

    public String getUserId() {
        return userId;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }

    public String getReviewContent() {
        return reviewContent;
    }

    public void setReviewContent(String reviewContent) {
        this.reviewContent = reviewContent;
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
