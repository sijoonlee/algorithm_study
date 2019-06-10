package com.sijoonlee;

public class Main {

    public static void main(String[] args) {

        int[] arr = { 1, 9, 3, 2, 0, 5, 8, 7 };

        int[] bubbleSortedArr = BubbleSort.Run(arr);

        Common.Print(bubbleSortedArr);

        int[] selectionSortedArr = SelectionSort.Run(arr);

        Common.Print(selectionSortedArr);

        int[] insertionSortedArr = InsertionSort.Run(arr);

        Common.Print(insertionSortedArr);

        int[] mergeSortedArr = MergeSort.Run(arr);

        Common.Print(mergeSortedArr);

        int[] quickSortedArr = QuickSort.Run(arr);

        Common.Print(quickSortedArr);
    }
}
