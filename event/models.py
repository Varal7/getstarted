from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.mail import send_mail

# Create your models here.
class Event(models.Model):
    name = models.CharField("Nom de l'événement", max_length=254, default="Get Started")

    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Activer pour lancer les inscriptions'
        ),
    )

    created = models.DateTimeField(_('Created'), auto_now_add=True, editable=False)
    modified = models.DateTimeField(_('Modified'), auto_now=True, editable=False)
    hits = models.PositiveIntegerField(_('Hits'), default=0)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Startup(models.Model):
    name = models.CharField("Nom de la stat-up", max_length=254)
    description = models.TextField("Description", blank=True)
    image = models.FileField("Image :", upload_to='startups')
    def __str__(self):              # __unicode__ on Python 2
        return self.name



class Participant(models.Model):
    username = models.CharField(
    "Nom d'utilisateur",
    max_length=254,
    # unique=True,
    help_text=_('Required. 254 characters or fewer. Letters, digits and @/./+/-/_ only.'),
    validators=[
        validators.RegexValidator(
            r'^[\w.@+-]+$',
            _('Enter a valid username. This value may contain only '
              'letters, numbers ' 'and @/./+/-/_ characters.')
        ),
    ],
    error_messages={
        # 'unique': _("Tu es déjà inscrit"),
    },
    )
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    email = models.EmailField(_('email address'),
    # unique=True,
     error_messages={
    # 'unique': "Un autre utilisateur a déjà cette adresse de courriel."
    })
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    last_visit = models.DateField(auto_now=True)

    promo = models.CharField("Promotion", max_length=30)

    BOOL_CHOICES = ((True, _('Yes')), (False, _('No')))
    found_stage = models.BooleanField("As-tu trouvé ton prochain stage ?", choices=BOOL_CHOICES, default=1)
    want_cocktail = models.BooleanField("Souhaites-tu participer au cocktail ?", choices=BOOL_CHOICES, default=0)


    YEAR_IN_SCHOOL_CHOICES = (
    ('2', '2A'),
    ('3', '3A'),
    ('M', 'Master'),
    ('D', 'Doctorat'),
            )

    year_in_school =  models.CharField("Ton niveau d'études",max_length=2,
                                      choices=YEAR_IN_SCHOOL_CHOICES,
                                      default=2)

    domains = models.TextField("Quels domaines t'intéresseraient ?", blank=True)

    missions = models.TextField("Quels types de missions souhaiterais tu mener en stage ?", blank= True)

    def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'user_{0}/{1}'.format(instance.username, filename)

    cv = models.FileField("Ton CV (format .pdf) :", upload_to=user_directory_path)



    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):              # __unicode__ on Python 2
        return self.first_name + ' ' + self.last_name
