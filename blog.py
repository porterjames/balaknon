from app import app, db
from app.models.site_user import SiteUser
from app.models.post import Post
from app.models.author import Author
from app.models.geo import Language, Country


@app.shell_context_processor
def make_shell_context():
    return {'db': db,
            'SiteUser': SiteUser,
            'Post': Post,
            'Author': Author,
            'Language': Language,
            'Country': Country}


# This file is part of Balaknon.
#
# Balaknon is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Balaknon is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Balaknon.  If not, see <https://www.gnu.org/licenses/>.
