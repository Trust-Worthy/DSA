use super::Sorter;


pub struct  Bubblesort;


impl Sorter for Bubblesort {
    
    
    fn sort<T>(slice: &mut [T]) where T: Ord {
        
        // TO-DO
      
        let mut swapped = true;
        // Keep doing this until entire array is walked without having to set 
        // swapped to true!
        while swapped {
            swapped = false;

            for i in 0..(slice.len() - 1) { // doing slice.len() - 1 to stay within bounds
                if slice[i] > slice[i + 1] {
                    slice.swap(i, i+1);
                    swapped = true;
                }
            }
        }

        
    }

}


#[test]
    fn bubble_sort_works() {
        let mut things = vec![4,2,5, 3,1];
        super::sort::<_,Bubblesort>(&mut things);
        assert_eq!(things, &[1,2,3,4,5]);
    }

