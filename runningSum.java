/*1480. Running sum of 1D array*/


class Solution {
    public int[] runningSum(int[] num) {   
        int[] rsum=new int[num.length];   
        rsum[0]=num[0];                    // array at 0th place will start same as given in array.
        for (int i=1 ;i<num.length;i++){  // adding starts from 1th place of array
            rsum[i]=num[i]+rsum[i-1];     
        }
        return rsum;
    }
    
}
