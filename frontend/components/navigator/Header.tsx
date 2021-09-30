import { FC } from "react"
import {
  Stack,
  Heading,
  Flex,
  Text,
} from "@chakra-ui/react"

const Header: FC = () => {
  return (
    <Flex
      as="nav"
      align="center"
      justify="space-between"
      wrap="wrap"
      padding={4}
      bg="teal.500"
      color="white"
    >
      <Flex align="center" mr={5}>
        <Heading as="h1" size="lg" letterSpacing={"tighter"}>
          ShareTimes
        </Heading>
      </Flex>
    </Flex>
  )
}

export default Header
