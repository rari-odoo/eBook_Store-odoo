from odoo import models, fields

class Book(models.Model):
    _name = "bookstore.book"
    _description = "Book Store Application"
    _log_access = False


    name = fields.Char("Book Title", required=True)
    expceted_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price", readonly = False)
    year = fields.Date("Year", required = True )
    description  = fields.Text("Description")
    email = fields.Char("Email")
    contact_no = fields.Integer("Contact Number")
    isbn_code = fields.Integer("ISBN code")
    state = fields.Selection([('publish','Publish'),('unpublish','Unpublish')], string="Status")
    publish_id = fields.Many2one("bookstore.publish", "Publisher")
    author_id = fields.Many2one("bookstore.author", string="Author" )
    book_type_id = fields.Many2one("bookstore.book.type",string="Book Type")
    