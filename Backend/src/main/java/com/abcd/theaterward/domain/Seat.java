package com.abcd.theaterward.domain;


import jakarta.persistence.*;

@Entity
@Table(name = "seat")
public class Seat {

    @Id
    @Column(name = "theater_no")
    private int theaterNo;

    @Id
    @Column(name = "seat_no")
    private int seatNo;

    @Column(name = "seat_row")
    private int seatRow;

    @Column(name = "seat_col")
    private int seatCol;

    @Column(name = "seat_floor")
    private int seatFloor;

    @Column(name = "seat_coord")
    private String seatCoord;

    @Column(name = "seat_keyword")
    private String seatKeyword;

    public String getSeatKeyword() {
        return seatKeyword;
    }

    public void setSeatKeyword(String seatKeyword) {
        this.seatKeyword = seatKeyword;
    }

    public String getSeatCoord() {
        return seatCoord;
    }

    public void setSeatCoord(String seatCoord) {
        this.seatCoord = seatCoord;
    }

    public int getSeatFloor() {
        return seatFloor;
    }

    public void setSeatFloor(int seatFloor) {
        this.seatFloor = seatFloor;
    }

    public int getSeatCol() {
        return seatCol;
    }

    public void setSeatCol(int seatCol) {
        this.seatCol = seatCol;
    }

    public int getSeatRow() {
        return seatRow;
    }

    public void setSeatRow(int seatRow) {
        this.seatRow = seatRow;
    }

    public int getSeatNo() {
        return seatNo;
    }

    public void setSeatNo(int seatNo) {
        this.seatNo = seatNo;
    }

    public int getTheaterNo() {
        return theaterNo;
    }

    public void setTheaterNo(int theaterNo) {
        this.theaterNo = theaterNo;
    }
}
