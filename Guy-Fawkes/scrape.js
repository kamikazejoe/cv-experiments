const Scraper = require('images-scraper');
const fs      = require('fs');
const request = require('request');
const Promise = require('bluebird');

var scraper = new Scraper.Bing();

scraper.list({
	keyword: 'guy fawkes mask',
	num: 1000,
})
.map(link => link.url)
.map(url => {
	return new Promise((resolve, reject) => {
		const match      = /^.*\/(.*)$/.exec(url);
		const filename   = match[1];
		const outputFile = fs.createWriteStream('./guyImages/'+filename);
		
		const req = request(url)

		req.on('error', reject);
		outputFile.on('error', reject);

		req.on('end', () => resolve());
		outputFile.on('end', () => resolve());

		req.pipe(outputFile);
	})
	.then(() => console.log('file downloaded'));
}, {concurrency: 10})
