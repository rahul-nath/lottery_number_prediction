import os
import webapp2
import jinja2
import lottery_ticket_gen

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)


class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
			self.write(self.render_str(template, **kw))

class MainPage(Handler):
	def get(self):
		self.render("index.html")

	def post(self):
		numbers = self.request.get("num_tickets")
		if numbers and numbers.isdigit():
			numbers = int(numbers)
			if numbers > 50:
				self.redirect("/error")
		else:
			self.redirect("/error")
		ticket_set = lottery_ticket_gen.gen_rand_tickets(numbers)
		self.render("lottery.html", ticket_set=ticket_set)



class LotteryNumbers(Handler):
	def get(self):
		self.render("lottery.html")

app = webapp2.WSGIApplication([('/', MainPage), ('/numbers', LotteryNumbers)], debug=True)
