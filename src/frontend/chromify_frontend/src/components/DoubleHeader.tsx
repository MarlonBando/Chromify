import { useState } from 'react';
import { Anchor, Box, Burger, Container, Group } from '@mantine/core';
import { useDisclosure } from '@mantine/hooks';
import classes from './DoubleHeader.module.css';
import { Image, Button } from '@mantine/core';
import { IconBrandGithub } from '@tabler/icons-react';

const userLinks = [
  { link: 'https://github.com/MarlonBando/Chromify', label: 'Github' },
];

const mainLinks = [
  { link: '#', label: 'Book a demo' },
  { link: '#', label: 'Documentation' },
  // { link: '#', label: 'Community' },
  { link: '#', label: 'Academy' },
  { link: '#', label: 'Forums' },
];

export function DoubleHeader() {
  const [opened, { toggle }] = useDisclosure(false);
  const [active, setActive] = useState(0);

  const mainItems = mainLinks.map((item, index) => (
    <Anchor<'a'>
      href={item.link}
      key={item.label}
      className={classes.mainLink}
      data-active={index === active || undefined}
      onClick={(event) => {
        event.preventDefault();
        setActive(index);
      }}
    >
      {item.label}
    </Anchor>
  ));

  const secondaryItems = (
    <Button
      component="a"
      href="https://github.com/MarlonBando/Chromify"
      target="_blank"
      variant="filled"
      color="rgba(0, 0, 0, 1)"
      size="lg"
      radius="md"
      leftSection={<IconBrandGithub size={30} />}
    >
      Repository
    </Button>
  );

  return (
    <header className={classes.header} >
      <Container className={classes.inner}>
      <Image
        radius="md"
        width={50}
        height={50}
        src="https://skaftenicki.github.io/dtu_mlops/figures/mlops_cycle.png"
      />
        <Box className={classes.links} visibleFrom="sm">
          <Group justify="flex-end">{secondaryItems}</Group>
          {/* <Group gap={0} justify="flex-end" className={classes.mainLinks}>
            {mainItems}
          </Group> */}
        </Box>
        <Burger
          opened={opened}
          onClick={toggle}
          className={classes.burger}
          size="sm"
          hiddenFrom="sm"
        />
      </Container>
    </header>
  );
}