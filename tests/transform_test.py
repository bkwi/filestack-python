import pytest

from httmock import urlmatch, HTTMock, response

from filestack import Filelink, Transform, AudioVisual
from filestack.config import CDN_URL

APIKEY = 'SOMEAPIKEY'
HANDLE = 'SOMEHANDLE'
EXTERNAL_URL = 'SOMEEXTERNALURL'


@pytest.fixture
def transform():
    return Transform(apikey=APIKEY, external_url=EXTERNAL_URL)


def test_sanity(transform):
    assert transform.apikey == APIKEY
    assert transform.external_url == EXTERNAL_URL
    assert hasattr(transform, 'delete')


def test_resize(transform):
    target_url = '{}/{}/resize=height:500,width:500/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    resize = transform.resize(width=500, height=500)
    assert resize.url == target_url


def test_crop(transform):
    target_url = '{}/{}/crop=dim:500/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    crop = transform.crop(dim=500)
    assert crop.url == target_url


def test_rotate(transform):
    target_url = '{}/{}/rotate=deg:90/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    rotate = transform.rotate(deg=90)
    assert rotate.url == target_url


def test_flip(transform):
    target_url = '{}/{}/flip/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    flip = transform.flip()
    assert flip.url == target_url


def test_flop(transform):
    target_url = '{}/{}/flop/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    flop = transform.flop()
    assert flop.url == target_url


def test_watermark(transform):
    target_url = '{}/{}/watermark=file:somefile.jpg/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    watermark = transform.watermark(file="somefile.jpg")
    assert watermark.url == target_url


def test_detect_faces(transform):
    target_url = '{}/{}/detect_faces=minsize:100/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    detect_faces = transform.detect_faces(minsize=100)
    assert detect_faces.url == target_url


def test_crop_faces(transform):

    target_url = '{}/{}/crop_faces=width:100/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    crop_faces = transform.crop_faces(width=100)
    assert crop_faces.url == target_url


def test_pixelate_faces(transform):
    target_url = '{}/{}/pixelate_faces=minsize:100/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    pixelate_faces = transform.pixelate_faces(minsize=100)
    assert pixelate_faces.url == target_url


def test_round_corners(transform):
    target_url = '{}/{}/round_corners=radius:100/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    round_corners = transform.round_corners(radius=100)
    assert round_corners.url == target_url


def test_vignette(transform):
    target_url = '{}/{}/vignette=amount:50/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    vignette = transform.vignette(amount=50)
    assert vignette.url == target_url


def test_polaroid(transform):
    target_url = '{}/{}/polaroid=color:blue/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    polaroid = transform.polaroid(color='blue')
    assert polaroid.url == target_url


def test_torn_edges(transform):
    target_url = '{}/{}/torn_edges/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    torn_edges = transform.torn_edges()
    assert torn_edges.url == target_url


def test_shadow(transform):
    target_url = '{}/{}/shadow=blur:true/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    shadow = transform.shadow(blur=True)
    assert shadow.url == target_url


def test_circle(transform):
    target_url = '{}/{}/circle=background:true/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    circle = transform.circle(background=True)
    assert circle.url == target_url


def test_border(transform):
    target_url = '{}/{}/border=width:500/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    border = transform.border(width=500)
    assert border.url == target_url


def test_sharpen(transform):
    target_url = '{}/{}/sharpen=amount:50/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    sharpen = transform.sharpen(amount=50)
    assert sharpen.url == target_url


def test_blur(transform):
    target_url = '{}/{}/blur=amount:10/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    blur = transform.blur(amount=10)
    assert blur.url == target_url


def test_monochrome(transform):
    target_url = '{}/{}/monochrome/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    monochrome = transform.monochrome()
    assert monochrome.url == target_url


def test_blackwhite(transform):
    target_url = '{}/{}/blackwhite=threshold:50/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    blackwhite = transform.blackwhite(threshold=50)
    assert blackwhite.url == target_url


def test_sepia(transform):
    target_url = '{}/{}/sepia=tone:80/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    sepia = transform.sepia(tone=80)
    assert sepia.url == target_url


def test_pixelate(transform):
    target_url = '{}/{}/pixelate=amount:10/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    pixelate = transform.pixelate(amount=10)
    assert pixelate.url == target_url


def test_oil_paint(transform):
    target_url = '{}/{}/oil_paint=amount:10/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    oil_paint = transform.oil_paint(amount=10)
    assert oil_paint.url == target_url


def test_negative(transform):
    target_url = '{}/{}/negative/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    negative = transform.negative()
    assert negative.url == target_url


def test_modulate(transform):
    target_url = '{}/{}/modulate=brightness:155,hue:155,saturation:155/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    modulate = transform.modulate(brightness=155, hue=155, saturation=155)
    assert modulate.url == target_url


def test_partial_pixelate(transform):
    target_url = (
        '{}/{}/partial_pixelate=amount:10,blur:10,'
        'objects:[[x,y,width,height],[x,y,width,height]],type:rect/{}'
    ).format(CDN_URL, APIKEY, EXTERNAL_URL)

    partial_pixelate = transform.partial_pixelate(
        amount=10, blur=10, type='rect', objects='[[x,y,width,height],[x,y,width,height]]'
    )
    assert partial_pixelate.url == target_url


def test_partial_blur(transform):
    target_url = (
        '{}/{}/partial_blur=amount:10,blur:10,'
        'objects:[[x,y,width,height],[x,y,width,height]],type:rect/{}'
    ).format(CDN_URL, APIKEY, EXTERNAL_URL)

    partial_blur = transform.partial_blur(
        amount=10, blur=10, type='rect', objects='[[x,y,width,height],[x,y,width,height]]'
    )
    assert partial_blur.url == target_url


def test_collage(transform):
    target_url = (
        '{}/{}/collage=autorotate:true,color:white,'
        'files:[FILEHANDLE,FILEHANDLE2,FILEHANDLE3],fit:crop,height:1000,margin:50,width:1000/{}'
    ).format(CDN_URL, APIKEY, EXTERNAL_URL)

    collage = transform.collage(
        files='[FILEHANDLE,FILEHANDLE2,FILEHANDLE3]', margin=50, width=1000, height=1000, color='white',
        fit='crop', autorotate=True
    )
    assert collage.url == target_url


def test_upscale(transform):
    target_url = '{}/{}/upscale=noise:low,style:artwork/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    upscale = transform.upscale(noise='low', style='artwork')
    assert upscale.url == target_url


def test_enhance(transform):
    target_url = '{}/{}/enhance/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    enhance = transform.enhance()
    assert enhance.url == target_url


def test_redeye(transform):
    target_url = '{}/{}/redeye/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    redeye = transform.redeye()
    assert redeye.url == target_url


def test_ascii(transform):
    target_url = (
        '{}/{}/ascii=background:black,colored:true,foreground:black,reverse:true,size:100/{}'
    ).format(CDN_URL, APIKEY, EXTERNAL_URL)

    ascii = transform.ascii(background='black', foreground='black', colored=True, size=100, reverse=True)
    assert ascii.url == target_url


def test_zip_no_store(transform):
    content = 'somecontent'

    @urlmatch(netloc=r'cdn\.filestackcontent\.com', method='get', scheme='https')
    def zip(url, request):
        return response(200, content)

    with HTTMock(zip):
        zip_response = transform.zip()
        assert zip_response.text == content


def test_zip_store(transform):
    @urlmatch(netloc=r'cdn\.filestackcontent\.com', method='get', scheme='https')
    def zip(url, request):
        return response(200, {'url': 'https://cdn.filestackcontent.com/{}'.format(HANDLE)})

    with HTTMock(zip):
        zip_transform = transform.zip(store=True)
        assert isinstance(zip_transform, Filelink)
        assert zip_transform.handle == HANDLE


def test_fallback(transform):
    target_url = '{}/{}/fallback=cache:12,handle:fallbackHandle/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    result = transform.fallback(handle='fallbackHandle', cache=12)
    assert result.url == target_url


def test_pdf_info(transform):
    target_url = '{}/{}/pdfinfo=colorinfo:true/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    result = transform.pdf_info(colorinfo=True)
    assert result.url == target_url


def test_pdf_convert(transform):
    target_url = '{}/{}/pdfconvert=pageorientation:landscape/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    result = transform.pdf_convert(pageorientation='landscape')
    assert result.url == target_url


def quality(transform):
    target_url = '{}/{}/quality=value:75/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    quality = transform.quality(75)

    assert quality.url == target_url


def test_filetype_conversion(transform):
    target_url = (
        '{}/{}/output=background:white,colorspace:input,compress:true,density:50,docinfo:true,format:png,'
        'page:1,pageformat:legal,pageorientation:landscape,quality:80,secure:true,'
        'strip:true/{}'
    ).format(CDN_URL, APIKEY, EXTERNAL_URL)

    filetype_conversion = transform.filetype_conversion(
        format='png', background='white', page=1, density=50, compress=True,
        quality=80, strip=True, colorspace='input', secure=True,
        docinfo=True, pageformat='legal', pageorientation='landscape'
    )
    assert filetype_conversion.url == target_url


def test_no_metadata(transform):
    target_url = ('{}/{}/no_metadata/{}').format(CDN_URL, APIKEY, EXTERNAL_URL)

    no_metadata = transform.no_metadata()
    assert no_metadata.url == target_url


def test_store(transform):
    @urlmatch(netloc=r'cdn.filestackcontent\.com', method='get', scheme='https')
    def store(url, request):
        return response(200, {'url': 'https://cdn.filestackcontent.com/{}'.format(HANDLE)})

    with HTTMock(store):
        transform_obj = transform.flip()
        store = transform_obj.store(
            filename='filename', location='S3', path='/py-test/', container='filestack-test',
            region='us-west-2', access='public', base64decode=True
        )

    assert isinstance(store, Filelink)


def test_av_convert(transform):
    @urlmatch(netloc=r'process.filestackapi\.com', method='get', scheme='https')
    def av_convert(url, request):
        return response(200, {'url': url, 'uuid': 'someuuid', 'timestamp': 'sometimestamp'})

    with HTTMock(av_convert):
        new_av = transform.av_convert(width=500, height=500)
        assert isinstance(new_av, AudioVisual)
        assert new_av.uuid == 'someuuid'
        assert new_av.timestamp == 'sometimestamp'


def test_debug(transform):
    @urlmatch(netloc=r'cdn.filestackcontent\.com', method='get', scheme='https')
    def debug(url, request):
        return response(200, {'data': 'somedata'})

    with HTTMock(debug):
        debug_response = transform.resize(width=500, height=500).debug()
        assert debug_response['data'] == 'somedata'
