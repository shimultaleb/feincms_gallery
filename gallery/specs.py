from django.utils.translation import ungettext_lazy, ugettext_lazy as _

class Base(object):
    template_path = 'content/gallery'
    default_template = '%s/classiclm.html' % template_path
    paginated = False

    @property
    def templates(self):
        templates = [
            '%s/%s.html' % (self.template_path, self.__class__.__name__.lower()),
            self.default_template ]

        if hasattr(self, 'template_name'):
            templates.insert(0, '%s/%s' % (self.template_path, self.template_name))
        return templates

    @property
    def name(self):
        return self.__class__.__name__

    @classmethod
    def __init__(self, **kwargs):
        for arg in kwargs:
            setattr(self, arg, kwargs[arg])


class ClassicLightbox(Base):
    verbose_name = _('Classic Gallery with Lightbox.')
    paginated = True
    paginate_by = 12
    orphans = 3
    columns = 3
    template_name = 'p.classiclm.html'

    media = {
        'css': {'all': ('lib/fancybox/jquery.fancybox-1.3.1.css',
                        'content/gallery/classic.css')},
        'js': ('lib/fancybox/jquery.fancybox-1.3.1.pack.js',
               '/media/content/gallery/gallery.js'),
    }

DEFAULT_SPECS = (ClassicLightbox(),)

#TODO: write classes for all predefined gallery types:
#
#GALLERY_TYPE_CHOICES = (
#    #('p.classic' , _('Classic Gallery with full size lightbox.')),
#    #('p.clasiccaption' , _('Classic Gallery with caption and full size lightbox.')),
#    ('p.classiclm', _('Classic Gallery with Lightbox.')),
#    ('p.classiclmcaption', _('Classic Gallery with caption and Lightbox.')),
#    ('carousel', _('Single line Strip Board')),
#    ('panel', _('Fancy Panel')),
#    ('slideshow', _('Simple Slideshow')),
#    ('product', _('Product Gallery')),
#    )
#
#standard_gallery_media = {'css':{'all':('content/gallery/classic.css',)}}
#
#DEFAULT_FORM_MEDIA_DICT = {'gallery': {'css': {'all': ('lib/fancybox/jquery.fancybox-1.3.1.css', )},
#                                       'js': ('lib/fancybox/jquery.fancybox-1.3.1.pack.js',
#                                              '/media/content/gallery/gallery.js')},
#                           'gallery_p.classic': standard_gallery_media,
#                           'gallery_p.clasiccaption': standard_gallery_media,
#                           'gallery_p.classiclm': standard_gallery_media,
#                           'gallery_p.classiclmcaption': standard_gallery_media,
#                           'gallery_slideshow': {'css': {'all': ('content/gallery/slideshow.css',)},
#                                                 'js': ('content/gallery/slideshow.js',)},
#                           'gallery_carousel': {'css': {'all': ('content/gallery/carousel.css',)},
#                                                'js': ('content/gallery/jquery.infinitecarousel2.min.js',
#                                                       'content/gallery/carousel.js',)},
#                           'gallery_panel': {'js': (
#                           'content/gallery/jquery.panelgallery-2.0.0.min.js', 'content/gallery/panelgallery.js')},
#                           'gallery_product': {'css': {'all': ('content/gallery/product.css',)},
#                                               'js': ('content/gallery/jquery.infinitecarousel2.min.js',
#                                                      'content/gallery/product.js',)},
#
#                           }
