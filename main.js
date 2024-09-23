
///////////////

function loadPage(page) {
    let content = document.getElementById('content');
    let homeTab = document.getElementById('home-tab');
    let datavizTab = document.getElementById('dataviz-tab');
   

    // Reset active class
    homeTab.classList.remove('active');
    datavizTab.classList.remove('active');


    if (page === 'home') {
        content.innerHTML = `
            <h1>Welcome to the Home Page</h1>
            <p>This is the main content of the Home page.</p>
        `;
        homeTab.classList.add('active');
    } else if (page === 'dataviz') {
        content.innerHTML = `
            <h1>Dataviz</h1>
            <p>This is the main content of the Dataviz page.</p>
        `;
        datavizTab.classList.add('active');
 
    }
}


// Fetch data using async function
async function fetchData() {
    try {
        const response = await fetch('http://localhost:5001/api/data');
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}


fetchData()


/*
// Fetch data using async function
async function fetchData() {

    try {
        const response = await fetch('http://localhost:5000/api/data');
        const result = await response.json();
        //console.log(result);
        result_city = result.city.city
        //console.log(result_city);

        result_state = result.city.state_code
        //console.log(result.city.state_code);

        prop_array = result.city.geo_statistics.housing_market.by_prop_type;
        
        data_arr =[result_city, result_state]
        
        console.log(data_arr)

        for (let i = 0; i < prop_array.length;i++)
            {
            
                console.log(prop_array[i].attributes)
                console.log(prop_array[i].type)
            }

        
        
    } catch (error) {
        console.error(error);
    }
}

// Example of calling fetchData when needed
fetchData();
*/