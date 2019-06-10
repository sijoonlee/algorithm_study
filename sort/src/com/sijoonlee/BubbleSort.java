package com.sijoonlee;

public class BubbleSort{

    public static int[] Run(int[] arr){
        int[] newArr = Common.Copy(arr);

        boolean swapped = true;
        int length = newArr.length;
        int counter = 0;
        while(swapped){
            swapped = false;
            counter ++;
            for ( int i = 0; i < length - counter; i++){
                if(newArr[i] > newArr[i+1]) {
                    Common.Swap(newArr, i, i + 1);
                    swapped = true;
                }
            }
        }
        return newArr;

    }
}


