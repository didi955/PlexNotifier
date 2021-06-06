import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


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
    def getMailNewEpisodeHTML(season_nb: int, show_title: str, summary: str) -> str:
        html = """\
                <html>
                  <body>
                    <h2>Le dernier épisode de la """ + str(season_nb) + """e saison de """ + str(show_title) + """ vient d'etre ajouté !<br></h2>
                    <img src="">
                    <h4>Résumé:</h4>
                    <p>""" + str(summary) + """ <br></p>
                    <p><br>Ne manquez surtout pas la suite !</p> 
                  </body>
                </html>
                """
        return html

    @staticmethod
    def getMailNewEpisodeText(season_nb: int, show_title: str, summary: str) -> str:
        text = """\
        Le dernier épisode de la """ + str(season_nb) + """e saison de """ + str(show_title) + """ vient d'etre ajouté !
        Résumé:
        """ + str(summary) + """"
        Ne manquez surtout pas la suite !"""
        return text

    @staticmethod
    def getMailNewMovieHTML(movie_title: str, summary: str) -> str:
        html = """\
                    <html>
                      <body>
                        <h2>Le film """ + str(movie_title) + """ vient d'etre ajouté !<br></h2>
                        <img src=""><br>
                        <h4>Résumé:</h4>
                        <p>""" + str(summary) + """ <br></p>
                        <p><br>Ne le manquez surtout pas !</p> 
                      </body>
                    </html>
                    """
        return html

    @staticmethod
    def getMailNewMovieText(movie_title: str, summary: str) -> str:
        text = """\
            Le film """ + str(movie_title) + """ vient d'etre ajouté !
            Résumé:
            """ + str(summary) + """"
            Ne le manquez surtout pas !"""
        return text
