# architecture.py
from diagrams import Cluster, Diagram
from diagrams.aws.network import VPC, PublicSubnet, PrivateSubnet, NATGateway, InternetGateway
from diagrams.aws.compute import EC2 # Just for visualization

with Diagram("AWS VPC Architecture - Task A", show=False, direction="TB"):
    with Cluster("VPC (10.0.0.0/16)"):
        igw = InternetGateway("Internet Gateway")
        
        with Cluster("Availability Zone: eu-central-1a"):
            with Cluster("Public Subnet 1 (10.0.101.0/24)"):
                nat = NATGateway("NAT Gateway")
                
            with Cluster("Private Subnet 1 (10.0.1.0/24)"):
                app1 = EC2("App Instance")

        with Cluster("Availability Zone: eu-central-1b"):
            with Cluster("Public Subnet 2 (10.0.102.0/24)"):
                pass # Empty for simplicity
                
            with Cluster("Private Subnet 2 (10.0.2.0/24)"):
                app2 = EC2("App Instance")

        # Connections
        igw >> nat
        nat >> app1
        nat >> app2