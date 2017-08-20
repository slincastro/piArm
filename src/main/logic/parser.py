from src.main.domain.joint_partial import Joint_partial


class Parser:

    def to_joint(self, primitive_joint):
        joint_attributes = primitive_joint.split()
        joint_name = joint_attributes[0]
        joint_direction = joint_attributes[1]
        joint_value = int(joint_attributes[2])

        return Joint_partial(joint_name, joint_direction, joint_value)

    def get_joints(self, joints_input):
        primitive_joints = joints_input.split("-")
        joints = []

        for primitive_joint in primitive_joints:
            joint = self.to_joint(primitive_joint)
            joints.append(joint)

        return joints
