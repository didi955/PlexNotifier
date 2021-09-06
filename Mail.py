import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from plexapi.video import Episode
from plexapi.video import Movie

import MovieDB


class Mail:

    def __init__(self, smtp_host: str, port: int, mail: str, password: str):
        self.smtp_host = smtp_host
        self.port = port
        self.mail = mail
        self.password = password

    def sendmail(self, target_mails: list, subject: str, text: str, html: str):
        bcc = []
        for mail in target_mails:
            bcc.append(mail)
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = self.mail
        message["To"] = self.mail
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smtp_host, self.port, context=context) as server:
            server.login(self.mail, self.password)
            server.sendmail(
                self.mail, [self.mail] + bcc, message.as_string()
            )

    @staticmethod
    def getMailNewEpisodeHTML(episode: Episode) -> str:
        nb = episode.index
        show_title = episode.grandparentTitle
        season_nb = episode.parentIndex
        paths = episode.locations
        summary = episode.summary
        season_title = episode.show().originalTitle
        path_split = paths[0].split("/")
        poster_path = MovieDB.getShowPoster_URL(show_title)
        html = """\
                <html>
                  <body>
                    <h1>Le dernier épisode de la """ + str(season_nb) + """e saison de """ + str(show_title) + """ vient d'etre ajouté !<br></h1>
                    <img src=" """ + str(poster_path) + """ " alt="poster' width="300" height="300">
                    <h3>Résumé:</h3>
                    <p>""" + str(summary) + """ <br></p>
                    <p><br>Ne manquez surtout pas la suite !</p> 
                  </body>
                </html>
                """
        return html

    @staticmethod
    def getMailNewEpisodeText(episode: Episode) -> str:
        nb = episode.index
        show_title = episode.grandparentTitle
        season_nb = episode.parentIndex
        summary = episode.summary
        season_title = episode.show().originalTitle
        text = """\
        Le dernier épisode de la """ + str(season_nb) + """e saison de """ + str(show_title) + """ vient d'etre ajouté !
        Résumé:
        """ + str(summary) + """"
        Ne manquez surtout pas la suite !"""
        return text

    @staticmethod
    def getMailNewMovieHTML(movie: Movie) -> str:
        movie_title = movie.title
        summary = movie.summary
        poster_url = MovieDB.getMoviePoster_URL(movie_title)
        html = """\
                    <html>
                      <body>
                        <h1>Le film '""" + str(movie_title) + """' vient d'etre ajouté !<br></h1>
                        <img src=" """ + str(poster_url) + """ " alt="poster' width="300" height="300">
                        <h3>Résumé:</h3>
                        <p>""" + str(summary) + """ <br></p>
                        <p><br>Ne le manquez surtout pas !</p> 
                      </body>
                    </html>
                    """
        return html

    @staticmethod
    def getMailNewMovieText(movie: Movie) -> str:
        movie_title = movie.title
        summary = movie.summary
        text = """\
            Le film '""" + str(movie_title) + """' vient d'etre ajouté !
            Résumé:
            """ + str(summary) + """"
            Ne le manquez surtout pas !"""
        return text
