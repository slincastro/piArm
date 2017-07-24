from src.main.domain.joint import Joint


class Parser:

    def to_joint(self, primitive_joint):
        joint_attributes = primitive_joint.split()
        joint_name = joint_attributes[0]
        joint_direction = joint_attributes[1]
        joint_value = int(joint_attributes[2])

        return Joint(joint_name, joint_direction, joint_value)
