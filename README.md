The aim of this application is to create an API that caters to various user needs by utilizing data provided by the Ministry of Finance regarding fuel prices across different stations in France.

Upon launching the API, entering the returned address in the terminal (or using ctrl + click), replacing "0.0.0.0" with "localhost," and appending "docs/" at the end in the address bar leads to "http://localhost:8151/docs."

Once this address is entered, the user gains access to a FastAPI interface. This interface presents multiple functionalities categorized into two distinct groups: functionalities related to station search and functionalities associated with user accounts.

Under the first category, the initial three methods enable the discovery of nearest gas stations based on geographic coordinates (latitude, longitude) or an address, or finding all gas stations within a city. The proximity station search can be filtered by fuel type and/or service offered. Users can specify the maximum distance they are willing to travel (as the crow flies) and the number of stations they wish to display.

In the second set of functionalities, the creation and deletion of a user account are available. Each user can create multiple lists of favorite stations that they can manage at their discretion. They can add or remove a station from any of these preferred lists.

It's important to note that the login feature could not be implemented. However, had it been possible, nearly all other functionalities would have been slightly modified. For instance, accessing or modifying a list of favorite stations would have been done only through a connected account associated with the specific list.

Let's illustrate the application's functionality with a practical example. Consider a scenario where a user commutes to work by car. Accidentally forgetting to refuel at their usual station, they need to refuel. Using our API, the user can search for the nearest gas stations to their workplace (by entering the address) that still have the desired fuel type available. Additionally, they intend to wash their vehicle, so they specify in the search "Laverie" and "SP95" (assuming their vehicle operates on SP95).

Preparing for a vacation, the same user wishes to plan their trip. Due to their vehicle's small fuel tank capacity, they want to identify stations they can visit in advance. Since they plan to pass through Lyon during their journey, they crceate an account on our API, establish a preferred stations list named "Vacation," and add the suitable gas station in Lyon (which they might have found earlier using the method to display all stations in a city). Now they are all set to embark on a delightful vacation!