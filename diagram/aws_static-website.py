# filename: aws_static-website.py
#
# pip install diagrams
# Requiere Graphviz instalado: https://graphviz.org/download/

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import User

from diagrams.aws.network import  CloudFront
from diagrams.aws.storage import S3

# Renderiza de izquierda a derecha
with Diagram("Static Website", show=False, outformat=["png"]) as diag:

    usuario = User("Usuario")

     # Nube AWS 
    with Cluster("AWS Cloud"):
        # Servicios “globales” (fuera de la región)
        cf = CloudFront("Amazon CloudFront")
        # Servicios en región
        with Cluster("Región: virginia (us-east-1)"):
            s3 = S3("Amazon S3\n(Sitio estático)")

    # Flujo de usuario y entrega de contenido
    usuario >> cf >> Edge(label="GET") >> s3

