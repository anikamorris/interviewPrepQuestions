// Print the lyrics to that beloved classic, that field-trip favorite: 99 Bottles of Beer on the Wall.

// No inputs, just print the song
// I can create 2 closures, one for each part of the verse, that take the number as a parameter to return the correct string
// Iterate through numbers from 99-1, but since I can't have a decreasing range in Swift, I'll go 1-99 and subract from 100
// Start the song with first phrase so I can keep the same number for each iteration
// That means that I'll have to add the last phrase on the end manually
// Handle the special cases in if statements inside the closures

func beer_song() {
        
    let phrase1: (Int) -> String = { num in
        if num > 1 {
            return "\nTake one down and pass it around, \(num) bottles of beer on the wall. "
        } else if num > 0 {
            return "\nTake one down and pass it around, \(num) bottle of beer on the wall."
        } else {
            return "\nTake it down and pass it around, no more bottles of beer on the wall."
        }
    }
    
    let phrase2: (Int) -> String = { num in
        if num > 1 {
            return "\(num) bottles of beer on the wall, \(num) bottles of beer."
        } else if num > 0 {
            return "\(num) bottle of beer on the wall, \(num) bottle of beer."
        } else {
            return "No more bottles of beer on the wall, no more bottles of beer."
        }
    }
    
    var song: String = phrase2(99)
    
    for i in 96...100 {
        let num = 100-i
        song += phrase1(num)
        song += "\n"
        song += phrase2(num)
    }
    
    song += "\nGo to the store and buy some more, 99 bottles of beer on the wall."
    
    print(song)
}

beer_song()
