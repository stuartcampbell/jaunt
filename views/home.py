import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates

templates = Jinja2Templates('templates')
router = fastapi.APIRouter()


@router.get('/', include_in_schema=False)
async def index(request: Request):
    data = {'request': request }
    return templates.TemplateResponse('index.html', data)
