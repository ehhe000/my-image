from http import HTTPStatus
import dashscope

model = "flux-schnell"

def generate_image_url(prompt):
    rsp = dashscope.ImageSynthesis.call(model=model,
                                        prompt=prompt,
                                        size='1024*1024')
    if rsp.status_code == HTTPStatus.OK:
        # 只返回链接
        for result in rsp.output.results:
            return result.url
    else:
        return f'Failed, status_code: {rsp.status_code}, code: {rsp.code}, message: {rsp.message}'