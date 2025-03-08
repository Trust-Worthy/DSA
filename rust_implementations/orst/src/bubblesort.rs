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

            for i in 0..slice.len() {
                if slice[i] > slice[i + 1] {
                    slice.swap(i, i+1);
                    swapped = true;
                }
            }
        }

        
    }

}

