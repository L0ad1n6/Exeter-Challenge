const express = require("express")
const session = require('express-session')
const path = require("path")
const bodyParser= require("body-parser")

const app = express();
app.use(bodyParser.urlencoded({extended:true}))
app.use(session({
	secret: "challenge",
	prev: 1,
	stage_1: false,
	stage_2: false,
	stage_3: false,
	stage_4: false,
	stage_5: false,
	resave: false,
  	saveUninitialized: true
}))


// var name = 't05e5gd3a3yibvxfrpu6';
// var hash = crypto.createHash('sha256').update(name).digest('hex');
// console.log(hash);

app.get("/", (req, res) => {
	res.redirect("/stage-1")
})

app.post("/token/", (req, res) => {
	let token = req.body.token
	if (token == "ZqDXWleKTNoYYBOrSCxM") {
		req.session.stage_1 = true
		req.session.prev = 2
		res.redirect("/stage-2")
	} else if (token == "BBIHjGIKFpYxZxjykdLQ") {
		req.session.stage_2 = true
		req.session.prev = 3
		res.redirect("/stage-3")
	} else if (token == "DAQnbfDumRragIjjDSZe") {
		req.session.stage_3 = true
		req.session.prev = 4
		res.redirect("/stage-4")
	} else if (token == "yhvgfodkvlreokkccuxv") {
		req.session.stage_4 = true
		req.session.prev = 5
		res.redirect("/stage-5")
	} else if (token == "HPIqaiJWoWlDhYfpUzMX") {
		req.session.stage_5 = true
		req.session.prev = 6
		res.redirect("/congrats")
	} else {
		switch (req.session.prev) {
			case 1:
				res.redirect("/stage-1")
				break;
			
			case 2:
				res.redirect("/stage-2")
				break;

			case 3:
				res.redirect("/stage-3")
				break;

			case 4:
				res.redirect("/stage-4")
				break;

			case 5:
				res.redirect("/stage-5")
				break;

			case 6:
				res.redirect("/congrats")
				break;

			default:
				res.redirect("/stage-1")
				break;
		}
	}
});

app.get("/stage-1", (req, res) => {
	res.sendFile("/views/stage-1.html", {root:path.join(path.resolve(__dirname, ".."))})
})

app.get("/stage-2", (req, res) => {
	if (!req.session.stage_1) {
		res.redirect("/stage-1")
	}
	res.sendFile("/views/stage-2.html", {root:path.join(path.resolve(__dirname, ".."))})
})

app.get("/stage-3", (req, res) => {
	if (!req.session.stage_2) {
		res.redirect("/stage-2")
	}
	res.sendFile("/views/stage-3.html", {root:path.join(path.resolve(__dirname, ".."))})
})

app.get("/stage-4", (req, res) => {
	if (!req.session.stage_3) {
		res.redirect("/stage-3")
	}
	res.sendFile("/views/stage-4.html", {root:path.join(path.resolve(__dirname, ".."))})
})

app.get("/stage-5", (req, res) => {
	if (!req.session.stage_3) {
		res.redirect("/stage-3")
	}
	res.sendFile("/views/stage-5.html", {root:path.join(path.resolve(__dirname, ".."))})
})

app.get("/congrats", (req, res) => {
	if (!req.session.stage_3) {
		res.redirect("/stage-3")
	}
	res.sendFile("/views/congrats.html", {root:path.join(path.resolve(__dirname, ".."))})
})

app.listen(3000);