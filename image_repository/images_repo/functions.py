from .API_keys import CLARIFAI_API_KEY, APPLICATION_ID
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import service_pb2_grpc
from clarifai_grpc.grpc.api import service_pb2, resources_pb2




def check_image_nsfw(form):
    image_bytes = form['image'].value().read()
    is_nsfw = False
    stub = service_pb2_grpc.V2Stub(ClarifaiChannel.get_grpc_channel())
    metadata =(("authorization", f"Key {CLARIFAI_API_KEY}"),)
    clarifai_request = service_pb2.PostModelOutputsRequest(
    model_id="nsfw-recognition",
    user_app_id=resources_pb2.UserAppIDSet(app_id=APPLICATION_ID),
    inputs=[
        resources_pb2.Input(
            data=resources_pb2.Data(image=resources_pb2.Image(base64=image_bytes)))],)
    clarifai_response = stub.PostModelOutputs(clarifai_request, metadata=metadata)
    concepts = clarifai_response.outputs[0].data.concepts
    for concept in concepts:
        if concept.name == 'nsfw':
            if concept.value > 0.7:
                is_nsfw = True
   
    return is_nsfw