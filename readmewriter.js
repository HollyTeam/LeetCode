/**
 * 自动生成readme脚本工具，用来应对写readme索引很麻烦的问题
 */

const fs = require('fs')
const cheerio = require('cheerio')

class Writer{
	constructor(config){
		this.config = Object.assign(Writer.defaultConfig(),config)
	}

	exec(){
		let txt = ''
		for(let i in this.config){
			txt += this.config[i]+'\n'
		}
		fs.writeFile('README.md',txt,'utf-8',function(err){
			if(err){
				throw err
			}
		})
	}
	/**
	 * @param {[]} arr
	 */
	load(arr,callback){
		let str = ''
		let format = {}
		for(let item of arr){
			str += `| ${item.index} | [${item.qname}](${item.qurl}) | [Python](${encodeURI(item.pyurl)}) | [Js](${encodeURI(item.jsurl)}) | ${item.hard} |\n`
		}
		this.config.body = str
		if(callback)
			callback()
	}
	/**
	 * 预处理
	 * 将输入数据转化成可供load处理的数组
	 */
	preprocess(callback){
		fs.readFile('1.log','utf-8',(err, data) => {
			if(err){
				throw err
			}
			const $ = cheerio.load(data)
			let cont = []
			$('.reactable-data').children().each(function(){
				let index = $(this).children().eq(1).html()				// 1
				let qname = $(this).children().eq(2).find('a').text().replace(/\(/g,'').replace(/\)/g,'')	// Two Sum
				let url = $(this).children().eq(2).find('a').attr('href')	// /problems/two-sum
				let jsname = qname.toLowerCase().replace(/ /g,'-')		// two-sum
				cont.push({
					index,
					qname: $(this).children().eq(2).find('a').text(),
					qurl: `https://leetcode.com${url}`,
					pyurl: `https://github.com/HollyTeam/Leetcode/blob/master/Python/${index}. ${qname}/solution.py`,
					jsurl: `https://github.com/HollyTeam/Leetcode/blob/master/Js/${index}. ${qname}/${jsname}.js`,
					hard: $(this).children().eq(-2).find('span').text()
				})
			})
			if(callback)
				callback(cont)

		})
	}
	/**
	 * 创建文件
	 */
	createFiles(){

	}
}

Writer.defaultConfig = () => {
	return {
		header: `
# Leetcode Solutions with Python/JavaScript
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License](https://img.shields.io/badge/JavaScript-ES6-blue.svg)]()
[![License](https://img.shields.io/badge/Python-3.x-blue.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.md)`,
		body_pre:`
### LeetCode Algorithm

| # | Title | Python | Js | Difficulty |
|:---:|:---:|:---:|:---:|:---:|`,
		body:`
		`,
		footer:`
### Collaborators
* [@HuangZhenyang](https://github.com/HuangZhenyang)
* [@regaliastar](https://github.com/regaliastar)

### License
MIT`,
	}
}

const writer = new Writer({})

new Promise((resolve,reject) => {
	writer.preprocess(cont => {
		resolve(cont)
	})
})
.then(cont => {
	writer.load(cont)
})
.then(() => {
	writer.exec()
})
.catch(err => {
	console.log(err)
})
