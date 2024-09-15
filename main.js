const data = null;

const xhr = new XMLHttpRequest();
xhr.withCredentials = true;

xhr.addEventListener('readystatechange', function () {
	if (this.readyState === this.DONE) {
		console.log(this.responseText);
	}
});

xhr.open('GET', 'https://us-real-estate-listings.p.rapidapi.com/property/marketTrends?property_url=https%3A%2F%2Fwww.realtor.com%2Frealestateandhomes-detail%2F2433-S-Ramona-Cir_Tampa_FL_33612_M56257-22633');
xhr.setRequestHeader('x-rapidapi-key', 'Sign Up for Key');
xhr.setRequestHeader('x-rapidapi-host', 'us-real-estate-listings.p.rapidapi.com');

xhr.send(data);